import re

newStrip = 'aaa"bbb" ccc"ddd"eee'
pattern = re.compile('["](.*?)["]')
print(pattern.findall(newStrip))
# ['bbb', 'ddd']

string222 = 'adcd<user@test.com>'
# pattern222 = re.compile('<([^>]+)')
pattern222 = re.compile('<(.+)>')
print(pattern222.findall(string222))
# ['user@test.com']




string333 = 'aaaaa2002年的第五场雪bbbb'
pattern333 = re.compile('第(.*)场雪')
print(pattern333.findall(string333))
# ['五']



string444 = 'frameworkPayload/THAppModule_Example.app/Frameworks/THSmartCustomServiceModule.framework/JSCSLocalizable.bundle/'
pattern444 = re.compile('Frameworks/(.*).framework')
print(pattern444.findall(string444))
# ['THSmartCustomServiceModule']