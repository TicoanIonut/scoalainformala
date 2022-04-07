# from itertools import accumulate
# import re
# z = 'https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/'
# z = z.sub('20', addone)

# def increment(s, inc):
#     return s.replace(str(inc), str(inc + 1))
#
# s = 'I have 366 friends on facebook'
# inc = 0
# print(increment(s, 6))

# count = 20
# url = "http://example20.com/"
# while count < 28:
#     count += 1
#     z = url.replace('20', str(count))
#     print(z)

url = "http://example20.com/"
for count in range(20, 28):
    z = url.replace('20', str(count))
    print(z)
