from model.noticiaModelo import Noticias

noticia1 = Noticias("Titulo", "Autor", "Texto", "Legenda", "DataEHora", "Categoria", 1)
noticia1.criarNoticia() #FEITO
print(Noticias.mostrarNoticias()) #FEITO
# print(Noticias.mostrarNoticias_por_id(1))
# noticia2 = Noticias.mostrarNoticias_por_id(2)
# noticia2.deletarNoticia()
# print(Noticias.mostrarNoticias()) #FEITO
# noticia3 = Noticias.mostrarNoticias_por_id(1)
# noticia3.setTitulo("a")
# noticia3.setAutor("b")
# noticia3.setTexto("c")
# noticia3.setLegenda("d")
# noticia3.setDataEHora("e")
# noticia3.setCategoria("f")
# noticia3.editarNoticia()
# print(Noticias.mostrarNoticias_por_id(1))
