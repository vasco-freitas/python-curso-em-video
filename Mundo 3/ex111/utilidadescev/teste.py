from moeda import summary
from dados import read_money

num = read_money('Enter the price: €')
 
summary(num,23,24)