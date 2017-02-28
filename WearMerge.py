open("Merged.csv", "w").write("".join(sorted((list(set(open("GlicemiaMisurazioni.csv").readlines() + open("GlicemiaWearMisurazioni.csv").readlines()))), reverse=True)))
