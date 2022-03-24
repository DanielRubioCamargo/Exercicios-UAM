package Extra;

public class Lamp {

    float price;
    int volts;
    String color;

    public Lamp(float price_,int volts_, String color_){
        this.price = price_;
        this.volts = volts_;
        this.color = color_;
    }

    public void light_on(){
        System.out.println("Lights ON!");
    }

    public void light_off(){
        System.out.println("Lights OFF!");
    }


}
