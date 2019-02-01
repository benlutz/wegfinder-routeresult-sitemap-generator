import time

datum = time.strftime("%Y-%m-%d")
ids = []
file = open("routexml.xml", "w")
file.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?><?xml-stylesheet type=\"text/xsl\" href=\"//wegfinder.at/main-sitemap.xsl\"?>\
<urlset xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:image=\"http://www.google.com/schemas/sitemap-image/1.1\" xsi:schemaLocation=\"http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd http://www.google.com/schemas/sitemap-image/1.1 http://www.google.com/schemas/sitemap-image/1.1/sitemap-image.xsd\" xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">")
file.close()

with open("stations.csv", "r") as stations:
    for station in stations:
        ids = station.strip().split(",")
        for i in range(0, len(ids)):
            start = ids[i]
            for z in range(0, len(ids)):
                ziel = ids[z]
                if ziel == start:
                    continue
                print("<url><loc>https://wegfinder.at/route/from/" + start + "/to/" + ziel + "/at/departure/now</loc><lastmod>" + datum + "</lastmod><changefreq>always</changefreq></url>")
                file = open("routexml.xml", "a")
                file.write("<url><loc>https://wegfinder.at/route/from/" + start + "/to/" + ziel + "/at/departure/now</loc><lastmod>" + datum + "</lastmod><changefreq>always</changefreq></url>" + "\n")
    file.write("</urlset>")
    file.close()
