def number_to_month(month):
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
              "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "error"
print(number_to_month(0))
