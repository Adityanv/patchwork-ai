package com.patchwork.payment;

import java.util.List;

public class PaymentService {

    public void processPayment() {
        validatePayment();
    }

    public boolean validatePayment() {
        return true;
    }

    class PaymentValidator {
        public void validate() {
            System.out.println("Validating payment");
        }
    }
}