

#LEGB rule 
#LOCAL

# def report():
#     x ='local'
#     print(x)

#ENCLOSING

x = 'this is global'
def enclosing():
    x = 'enclosing '

    def inside():
        print(x)

    inside()

enclosing()


#GLOBAL
#BUILT IN



