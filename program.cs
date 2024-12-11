
#using System;

// Definición de la clase Producto para gestionar los datos de un producto
public class Producto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string Unidad { get; set; }
    public decimal[] Precios { get; set; } = new decimal[3];
}
