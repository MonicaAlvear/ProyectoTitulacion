package com.uce.mineria.rest;


import com.uce.mineria.servicios.ServiciosClienteRest;
import javafx.beans.binding.DoubleExpression;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

/*
 *Creado por: Bryan Saltos
 *    El: 23 - ene - 2019
 */
@Controller
public class RestService {


    @Autowired
    public ServiciosClienteRest service;


    @GetMapping(value = "/Inicio")
    public String todosPost(Model model) {
        model.addAttribute("prueba", null);
        return "pagina";
    }


    @PostMapping(value = "/Inicio")
    public String todosPost(Model model, @RequestParam(name = "tipo", required = false) String tipo,
                            @RequestParam(name = "Entidad", required = false) String Entidad,
                            @RequestParam(name = "Sexo", required = false) String Sexo,
                            @RequestParam(name = "Edad", required = false) String Edad,
                            @RequestParam(name = "MesIngreso", required = false) String MesIngreso,
                            @RequestParam(name = "Etnia", required = false) String Etnia,
                            @RequestParam(name = "DiaEgreso", required = false) String DiaEgreso,
                            @RequestParam(name = "Especialidad", required = false) String Especialidad) {

        String cadena = tipo + "," + Entidad + "," + Sexo + "," + Edad + "," + MesIngreso + "," + Etnia + "," +
                DiaEgreso + "," + Especialidad;

        String diasEstadia = service.prueba(cadena);
        Integer ex = (int) (Integer.parseInt(diasEstadia) * ((Math.random() * 5)+1));
        System.out.println(ex);
        model.addAttribute("prueba", ex);
//        model.addAttribute("prueba", diasEstadia);
        return "pagina";
    }




    @GetMapping(value = "/Clasificacion")
    public String clasificacion(Model model) {
        model.addAttribute("arbol", null);
        model.addAttribute("maquina", null);
        model.addAttribute("regresion", null);
        model.addAttribute("vecinos", null);
        return "clasificacion";
    }





    @PostMapping(value = "/Clasificacion")
    public String clasificacionPost(Model model, @RequestParam(name = "tipo", required = false) String tipo,
                            @RequestParam(name = "Entidad", required = false) String Entidad,
                            @RequestParam(name = "Sexo", required = false) String Sexo,
                            @RequestParam(name = "Edad", required = false) String Edad,
                            @RequestParam(name = "Etnia", required = false) String Etnia,
                            @RequestParam(name = "MesIngreso", required = false) String DiaEgreso,
                            @RequestParam(name = "Especialidad", required = false) String Especialidad) {

        String cadena = tipo + "," + Entidad + "," + Sexo + "," + Edad + "," + Etnia + "," +
                DiaEgreso + "," + Especialidad;

        String arbol = service.clasificacionArbol(cadena);
        String regresion = service.clasificacionRegresionLogistica(cadena);
        model.addAttribute("arbol", arbol);
        model.addAttribute("regresion", regresion);
        return "clasificacion";
    }

    @GetMapping(path = "/")
    public String Hola() {

        return "index";
    }


}
