class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, helado):
        if helado.id not in self.carrito.keys():
            self.carrito[helado.id]={
                "helado_id":helado.id, 
                "rango": helado.rango,
                "sabor": helado.sabor,
                "precio": str (helado.precio),
                "cantidad": 1,
                "total": helado.precio,

            }
        else:
            for key, value in self.carrito.items():
                if key==helado.id:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = helado.precio
                    value["total"]= value["total"] + helado.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True

    def eliminar(self, helado):
        id = helado.id
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,helado):
        for key, value in self.carrito.items():
            if key == helado.id:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- helado.precio
                if value["cantidad"] < 1:   
                    self.eliminar(helado)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 