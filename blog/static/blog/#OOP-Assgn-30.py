#OOP-Assgn-30
#Start writing your code here
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity

    def get_customer_name(self):
        return self.__customer_name


    def get_quantity(self):
        return self.__quantity
   
    def validate_quantity(self):
        if self.get_quantity()>=1 and self.get_quantity()<=5:
            return True
        else:
            return False
         

class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None

    def get_service_id(self):
        return self.__service_id


    def get_customer(self):
        return self.__customer


    def get_pizza_type(self):
        return self.__pizza_type


    def get_additional_topping(self):
        return self.__additional_topping
   
    def validate_pizza_type(self):
        if self.get_pizza_type().lower()=='small' or self.get_pizza_type().lower()=='medium':
            return True
        else:
            return False
   
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            if self.get_additional_topping() and self.get_pizza_type().lower()=='small':
                add_tp=35
            elif self.get_additional_topping() and self.get_pizza_type().lower()=='medium':
                add_tp=50
            else:
                add_tp=0
            if self.get_pizza_type().lower()=='small':
                cost=150
            else:
                cost=200
            total=cost*self.get_customer().get_quantity()+add_tp*self.get_customer().get_quantity()
            self.pizza_cost=total
            Pizzaservice.counter+=1
            self.__service_id=self.get_pizza_type()[0]+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1
   
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__distance_in_kms=distance_in_kms
        self.__delivery_charge=None

    def get_distance_in_kms(self):
        return self.__distance_in_kms


    def get_delivery_charge(self):
        return self.__delivery_charge
   
    def validate_distance_in_kms(self):
        if self.get_distance_in_kms()>=1 and self.get_distance_in_kms()<=10:
            return True
        else:
            return False
       
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost!=-1:
                if self.get_distance_in_kms()<=5:
                    delivery =5*self.get_distance_in_kms()
                else:
                    delivery =25+(self.get_distance_in_kms()-5)*7
                self.pizza_cost=self.pizza_cost+delivery
            else:
                self.pizza_cost=-1
        else:
            self.pizza_cost=-1

       
       
c1=Customer("abc",2)  
p1=Pizzaservice(c1,'Large',True)
p1.validate_pizza_type()
p1.calculate_pizza_cost()
d1=Doordelivery(c1,'Large',True,2)
d1.calculate_pizza_cost()
    



