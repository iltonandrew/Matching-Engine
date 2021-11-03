book_buy = {}
book_sell = {}


def Trade(price, qty):
    return print(f"Trade, price: {price}, qty: {qty}")


def limit_buy(price, qty):
    if price in book_buy:
        book_buy[price] += qty
    else:
        book_buy[price] = qty
    if price in book_sell:
        if book_sell[price] >= qty:
            book_sell[price] -= qty
            (Trade(price, qty))


def limit_sell(price, qty):
    if price in book_sell:
        book_sell[price] += qty
    else:
        book_sell[price] = qty
    if price in book_buy:
        if book_buy[price] >= qty:
            book_buy[price] -= qty
            Trade(price, qty)


def market_buy(qty):
    if len(book_sell) == 0:
        return "No trades"
    else:
        price = max(book_sell.keys())
        if book_sell[price] >= qty:
            book_sell[price] -= qty
            return Trade(price, qty)
        else:
            qty_sold = book_sell[price]
            book_sell[price] = 0
            return Trade(price, qty_sold)


def market_sell(qty):
    if len(book_buy) == 0:
        return "No trades"
    else:
        price = min(book_buy.keys())
        if book_buy[price] >= qty:
            book_buy[price] -= qty
            return Trade(price, qty)
        else:
            qty_sold = book_buy[price]
            book_buy[price] = 0
            return Trade(price, qty_sold)


def main():
    while True:
        order = input()
        if order == "":
            break
        order = order.split()
        if order[0] == "limit":
            if order[1] == "buy":
                limit_buy(int(order[2]), int(order[3]))
            elif order[1] == "sell":
                limit_sell(int(order[2]), int(order[3]))
        elif order[0] == "market":
            if order[1] == "buy":
                market_buy(int(order[2]))
            elif order[1] == "sell":
                market_sell(int(order[2]))


if __name__ == "__main__":
    main()
