from pyspark.sql.functions import count

name='sridhar ramachandraiah'

print(len(name))
count=0

for i in name:
    count +=1
print(count)


