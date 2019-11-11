import sys


poi_set = set()
uuid_set = set()
with open(sys.argv[0]) as f:
    for line in f:
        fields = line.split(" ")
        for field in fields:
            val = long(field)
            if val < 2200000000L:
                poi_set.add(val)
            else:
                uuid_set.add(val)

with open(sys.argv[1], "w") as f:
    for poi in poi_set:
        f.write(str(poi) + " 1\n")
    for uuid in uuid_set:
        f.write(str(uuid) + " 2\n")