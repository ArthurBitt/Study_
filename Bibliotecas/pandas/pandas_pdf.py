import camelot


tables = camelot.read_pdf("C:\\Users\\arthu\\OneDrive\\Documentos\\Projetos\\Projetos de estudo\\Python\\Programas\\foo.pdf", pages='1',flavor= "stream")

# tables.export("foo.csv", f="csv", compress=True)
tables[0].to_csv('foo.csv')
