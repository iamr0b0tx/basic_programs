import json
from time import strftime, ctime

def show_logs(data, condition=None):
    if condition is None:
        condition = lambda time: True

    print("{:^12s} | {:^12s} | {:^4s} | {:^9s} | {:^15s} | {:^16s}".format("Client", "Product", "Qty", "Price", "Total", "Time"))
    print("-" * 84)

    for transaction in data:
        time = transaction['time']
        if not condition(time):
            continue

        client_name = transaction['customer_name']
        products = transaction['product']
        

        overall_total = 0
        for product in products:
            product_name = product['product_name']
            product_quantity = product['product_quantity']
            product_price = product['product_price']

            total = product_price * product_quantity
            overall_total += total

            total = f'{total:,.2f}'
            product_price = f'{product_price:,.2f}'
            print(f"{client_name:<12s} | {product_name:<12s} | {product_quantity:^4.0f} | {product_price:>9s} | {total:>15s} | {time:>16s}")
            client_name = ''

        overall_total = f'{overall_total:,.2f}'
        print("{:^12s} | {:^12s} | {:^4s} | {:^9s} | {:>15s} | {:>16s}"
              .format("", "", "", "", overall_total, time))
        print("-" * 84)

def save_data(client_name, product_information):

    DATA.append(
        {
            'customer_name': client_name,
            'product': product_information,
            'time': strftime("%d/%m/%Y %H:%M")
        }
    )


def end_program():
    '''
    backup data and quit program
    '''

    # back up data as json
    with open('cash_register_backup.json', 'w') as f:
        json.dump(DATA, f)

    # disp;ay all logs
    show_logs(DATA)

    # quit program
    exit()


def get_number_input(prompt):
    '''
    use prompt to collects input and return float
    '''

    # initialize value
    value = None

    # if collected value is not float
    while type(value) != float:
        try:
            value = float(input(prompt))
            return value

        except KeyboardInterrupt:
            end_program()

        except ValueError as e:
            print("Invalid Input!")
            print(ctime(), e, file=ERROR_FILE)


def main():
    while True:
        client_name = input('What is the customer\'s name?: ')
        if not client_name:
            print('Name must be provided!')
            continue

        elif client_name == '-1':
            end_program()

        # store all product details
        product_information = []

        while True:
            product_name = input('what is the product name?: ')

            if not product_name:
                print('Product name must be provided!')
                continue

            elif product_name == '-1':
                # end_program(client_name, product_information)
                save_data(client_name, product_information)
                break

            product_qty = get_number_input(
                f'How many {product_name} purchased?: ')
            if product_qty == -1:
                save_data(client_name, product_information)
                break

            product_price = get_number_input(f"How much is {product_name}?: ")
            if product_price == -1:
                # end_program(client_name, product_information)
                save_data(client_name, product_information)
                break

            product_information.append(
                {
                    'product_name': product_name,
                    'product_quantity': product_qty,
                    'product_price': product_price
                }
            )


if __name__ == '__main__':
    # superglobals
    ERROR_FILE = open('error_log.txt', 'a')
    DATA = []

    with open('cash_register_backup.json') as f:
        DATA = json.load(f)

    # the main code
    main()

    # close file
    ERROR_FILE.close()
