company_name = 'devopsdelight'
company_value_in_billions = 25.7
products_count = 10

print(company_name, company_value_in_billions, products_count)

print(company_name, company_value_in_billions, products_count, sep=":")

print(company_name, company_value_in_billions, products_count, end=" ")
print(company_name, company_value_in_billions, products_count)

print("company_value=%0.2f" %company_value_in_billions) # as the format is 0.2 value is rounded of two decimal digits

print("products_count=%8d" %products_count)  #right aligned within the reserved 8 spaces 

print("products_count=%-8d" %products_count) # left aligned within the reserved 8 spaces as there is – symbol

"""
output :

devopsdelight 25.7 10
devopsdelight:25.7:10
devopsdelight 25.7 10 devopsdelight 25.7 10
company_value=25.70
products_count=      10
products_count=10   
"""