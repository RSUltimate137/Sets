Zorgs = {"blip", "zorath", "quarn", "melo", "drak", "tula", "gloop", "venar"}
Blorps = {"gloop", "melo", "frint", "zabu", "drak", "snoot", "plar", "blarn"}

# print(A & B)   # intersection
# print(A - B)   # difference

#intersection
common = Zorgs.intersection(Blorps)
print(common)

#difference
unique = Zorgs.difference(Blorps)
print(unique)
unique1 = Blorps.difference(Zorgs)
print(unique1)

#union
combine = Zorgs.union(Blorps)
print(f"The total number of unique words is {combine}")