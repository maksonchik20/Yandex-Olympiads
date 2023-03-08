import sys


def way(city_from, city_to, path, price):
    if city_from == city_to:
        if price < way.best['price']:
            way.best["path"] = path
            way.best["price"] = price
        return
    roads = set(prices[city_from]) - set(path)
    if not roads:
        return
    if price > way.best["price"]:
        return
    for r in roads:
        way(r, city_to, path + [r], price + prices[city_from][r])


def best_way(city_from, city_to):
    way.best = {'path': [], 'price': 10000000}
    way(city_from, city_to, [city_from], 0)
    return way.best


if __name__ == "__main__":
    rows = [r for r in sys.stdin.read().split("\n") if r]
    f, to = rows[-1].split()
    prices = {}
    for r in rows[:-1]:
        a, b, price = r.split()
        price = int(price)
        if a not in prices:
            prices[a] = {}
        prices[a][b] = price
    print(", ".join([str(p) for p in best_way(f, to)["path"]]))
