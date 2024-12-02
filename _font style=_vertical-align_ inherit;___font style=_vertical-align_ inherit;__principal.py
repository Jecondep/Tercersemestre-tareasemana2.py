
Nombre: Johnny Edith Conde Paucar

Fecha: 15/12/2024

Número de Hoja: 1

using System;

// Clase que representa un círculo
public class Circulo
{
    // Propiedad que almacena el radio del círculo
    public double Radio { get; set; }

    // Constructor que inicializa el radio
    public Circulo(double radio)
    {
        Radio = radio;
    }

    // CalcularArea es una función que devuelve un valor double, se utiliza para calcular el área de un círculo, requiere como argumento el radio del círculo
    public double CalcularArea()
    {
        return Math.PI * Radio * Radio;
    }

    // CalcularPerimetro es una función que devuelve un valor double, se utiliza para calcular el perímetro de un círculo
    public double CalcularPerimetro()
    {
        return 2 * Math.PI * Radio;
    }
}

// Clase que representa un cuadrado
public class Cuadrado
{
    // Propiedad que almacena el lado del cuadrado
    public double Lado { get; set; }

    // Constructor que inicializa el lado
    public Cuadrado(double lado)
    {
        Lado = lado;
    }

    // CalcularArea es una función que devuelve un valor double, se utiliza para calcular el área de un cuadrado, requiere como argumento el lado del cuadrado
    public double CalcularArea()
    {
        return Lado * Lado;
    }

    // CalcularPerimetro es una función que devuelve un valor double, se utiliza para calcular el perímetro de un cuadrado
    public double CalcularPerimetro()
    {
        return 4 * Lado;
    }
}

// Ejemplo de uso
class Program
{
    static void Main(string[] args)
    {
        // Crear un objeto de la clase Circulo con un radio de 5
        Circulo circulo = new Circulo(5);
        Console.WriteLine("Área del círculo: " + circulo.CalcularArea());
        Console.WriteLine("Perímetro del círculo: " + circulo.CalcularPerimetro());

        // Crear un objeto de la clase Cuadrado con un lado de 4
        Cuadrado cuadrado = new Cuadrado(4);
        Console.WriteLine("Área del cuadrado: " + cuadrado.CalcularArea());
        Console.WriteLine("Perímetro del cuadrado: " + cuadrado.CalcularPerimetro());
    }
}