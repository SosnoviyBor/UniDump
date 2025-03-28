#include "stm32f103x6.h"
#include <string>

void init_ADC() {
    // enable ADC and make it continuous
    // p0 by default
    ADC1->CR2 |= ADC_CR2_ADON | ADC_CR2_CONT;
    ADC1->SMPR2 |= ADC_SMPR2_SMP0;
    ADC1->CR2 |= ADC_CR2_SWSTART; // launch ADC
}

void init_USART1n2() {
    // output USART
    // bound to p9 port cuz lord Jesus said so
    USART1->BRR = 8000000 / 9600; // baud rate
    USART1->CR1 |= USART_CR1_TE | USART_CR1_UE; // transmit and USART enable

    // input USART
    // bound to p3
    NVIC_EnableIRQ(USART2_IRQn);
    USART2->BRR = 8000000 / 9600;
    USART2->CR1 |= USART_CR1_RE | USART_CR1_UE; // recieve and USART enable
}

void init_timer(bool enabled) {
    NVIC_EnableIRQ(TIM2_IRQn);
    TIM2->PSC = 8000-1; // prescale clock to 1khz
    TIM2->ARR = 1000-1; // proc 1 sec
    TIM2->DIER = TIM_DIER_UIE; // enable interruptions
    if (enabled) {
        TIM2->CR1 = TIM_CR1_CEN;
    }
}

void init_PWM(bool enabled) {
    GPIOA->CRH &= ~(GPIO_CRH_MODE8 | GPIO_CRH_CNF8);
    GPIOA->CRH |= GPIO_CRH_MODE8_0 | GPIO_CRH_CNF8_1;
    AFIO->MAPR |= AFIO_MAPR_TIM1_REMAP_0; // make alt function proc on p7
    TIM1->PSC = 8000-1; // 1khz
    TIM1->ARR = 1000-1; // proc 1 sec
    TIM1->CCR1 = 250-1; // pulse length to 1/4 sec
    TIM1->CCER |= TIM_CCER_CC1E | TIM_CCER_CC1P; // enable capture/compare, invert polarity
    TIM1->BDTR |= TIM_BDTR_MOE; // enable output
    TIM1->CR1 |= TIM_CR1_CEN; // enable counter
    if (enabled) {
        TIM1->CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2;
    }
}

void send(char s) {
        while ((USART1->SR & USART_SR_TC) == 0); // wait for completion
        USART1->DR = s;
}

void send(std::string msg) {
    for (auto s : msg) {
        send(s);
    }
}

extern "C" void USART2_IRQHandler() { // Doesnt work for whatever fucking reason
    send("USART2 INTERRUPTION ACTUALLY WORKS WTFFFF\r\n");
    USART2->SR &= ~USART_SR_RXNE;
}

extern "C" void TIM2_IRQHandler() {
    send("Timer is up!\r\n");
    TIM2->SR &= ~TIM_SR_UIF; // reset the update ivent flag
}

int main() {
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN | RCC_APB1ENR_TIM2EN;
    RCC->APB2ENR |= RCC_APB2ENR_USART1EN | RCC_APB2ENR_IOPAEN | RCC_APB2ENR_ADC1EN | RCC_APB2ENR_TIM1EN;

    init_ADC();
    init_USART1n2();
    GPIOA->CRL |= GPIO_CRL_MODE1_0; // init LED lmao
    init_timer(false);
    init_PWM(false);

    send("I'm a reciever ma'am, not the other one.\r\n"
         "==========================\r\n"
         "Q - Show ADC\r\n"
         "W - Enable LED\r\n"
         "E - Disable LED\r\n"
         "R - Enable Timer Display\r\n"
         "T - Disable Timer Display\r\n"
         "Y - Enable PWM\r\n"
         "U - Disable PWM\r\n"
         "==========================\r\n"
         "1-5 - Set timer's delay to X seconds\r\n"
         "6-9 - Set PWM's pulse length to 1000-250*(X-1) miliseconds. Ugly, but what can you do\r\n"
         "==========================\r\n"
    );
    
    char tmp[200];
    int val;
    while (true) {
        switch (tolower(USART2->DR)) {
            case 'q': // show ADC
                snprintf(tmp, sizeof(tmp), "ADC = %d \r\n", int(ADC1->DR));
                send(std::string(tmp));
                break;
            
            case 'w': // Enable LED
                send("> Enabled LED!\r\n");
                GPIOA->BSRR = GPIO_BSRR_BS1;
                break;
            
            case 'e': // Disable LED
                send("> Disabled LED!\r\n");
                GPIOA->BSRR = GPIO_BSRR_BR1;
                break;
            
            case 'r': // Enable Timer
                send("> Enabled timer!\r\n");
                TIM2->CR1 = TIM_CR1_CEN;
                break;
            
            case 't': // Disable TImer
                send("> Disabled timer!\r\n");
                TIM2->CR1 = 0;
                break;
            
            case 'y': // Enable PWM
                send("> Enabled PWM!\r\n");
                TIM1->CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2;
                break;
            
            case 'u': // Disable PWM
                send("> Disabled PWM!\r\n");
                TIM1->CCMR1 &= ~(TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2);
                break;
            
            case '1': case '2': case '3': case '4': case '5':
                val = int(USART2->DR)-48; // 1-5
                snprintf(tmp, sizeof(tmp), "> Set timer's delay to %d sec!\r\n", val);
                send(tmp);
                TIM2->ARR = (int(USART2->DR)-48)*1000-1;
                break;
            
            case '6': case '7': case '8': case '9':
                val = int(USART2->DR)-5-48; // 1-4
                snprintf(tmp, sizeof(tmp), "> Set PWM's pulse length to %d milisec!\r\n", 1000-250*(val-1));
                send(tmp);
                TIM1->CCR1 = (1000-250*(val-1))-1; // pulse length from 1/1 sec to 1/4 sec
                break;
        }
        for (volatile int i = 0; i < 800000; i++); // improvised delay
    };

    return 0;
}