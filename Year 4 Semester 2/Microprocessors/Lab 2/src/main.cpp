#include "stm32f103x6.h"
#include <string>

void send(char s) {
        while ((USART1->SR & USART_SR_TC) == 0); // wait for completion
        USART1->DR = s;
}

void send(std::string msg) {
    for (auto s : msg) {
        send(s);
    }
}

std::string cmd;
extern "C" void USART2_IRQHandler() { // TODO Douesnt work for whatever fucking reason
    send("woop woop");
    cmd.push_back(USART2->DR);
    USART2->SR &= ~USART_SR_RXNE;
}

int main() {
    RCC->APB1ENR |= RCC_APB1ENR_USART2EN;
    RCC->APB2ENR |= RCC_APB2ENR_USART1EN | RCC_APB2ENR_IOPAEN | RCC_APB2ENR_ADC1EN;

    // enable ADC and make it continuous
    // p0 by default
    ADC1->CR2 |= ADC_CR2_ADON | ADC_CR2_CONT;
    ADC1->SMPR2 |= ADC_SMPR2_SMP0;
    ADC1->CR2 |= ADC_CR2_SWSTART; // launch ADC

    // output USART
    // bound to p9 port cuz lord Jesus said so
    USART1->BRR = 8000000 / 9600; // baud rate
    USART1->CR1 |= USART_CR1_TE | USART_CR1_UE; // transmit and USART enable

    // input USART
    // bound to p3
    USART2->BRR = 8000000 / 9600;
    USART2->CR1 |= USART_CR1_RE | USART_CR1_UE; // recieve and USART enable
    NVIC_EnableIRQ(USART2_IRQn);

    send("I'm a reciever, not the other guy!\r\n");
    while (true) {
        // display ADC
        // char tmp[200];
        // snprintf(tmp, sizeof(tmp), "ADC = %d \r\n", ADC1->DR);
        // send(std::string(tmp));
        send("cmd = " + cmd + "\r\n");
        for (volatile int i = 0; i < 80000; i++); // improvised delay
    };

    return 0;
}