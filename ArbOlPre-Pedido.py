class ArbolPrePedido:
    def __init__(self, Value):
        self.value = Value
        self.left = None
        self.rigth = None
        
def pre_order_traversal(node):
     if node is not None:
        print(node.value) # Visitar el nodo actual
        pre_order_traversal(node.left) # Recorrido del sub árbol izquierdo
        pre_order_traversal(node.rigth) # Recorrido del Sub árbol derecho
            
# Crear un árbol de ejemplo
root = ArbolPrePedido(1)
root.left = ArbolPrePedido(2)
root.rigth = ArbolPrePedido(3)
root.left.left = ArbolPrePedido(4)
root.left.rigth = ArbolPrePedido(5)  
root.rigth.left = ArbolPrePedido(6) 
root.rigth.rigth = ArbolPrePedido(7)    

# Realizar el recorrido en pre-pedido 
pre_order_traversal(root)
        