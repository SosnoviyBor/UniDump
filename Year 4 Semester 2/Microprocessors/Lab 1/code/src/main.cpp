#include "stm32f103x6.h"

void init_leds() {
    GPIOA->CRL |= GPIO_CRL_MODE0_0;
    GPIOA->CRL |= GPIO_CRL_MODE1_0;
    GPIOA->CRL |= GPIO_CRL_MODE2_0;
    GPIOA->CRL |= GPIO_CRL_MODE3_0;
    GPIOA->CRL |= GPIO_CRL_MODE4_0;
    GPIOA->CRL |= GPIO_CRL_MODE5_0;
    GPIOA->CRL |= GPIO_CRL_MODE6_0;
    // GPIOA->CRL |= GPIO_CRL_MODE7_0;
    // GPIOA->CRH |= GPIO_CRH_MODE8_0;
    GPIOA->CRH |= GPIO_CRH_MODE9_0;
    GPIOA->CRH |= GPIO_CRH_MODE10_0;
    GPIOA->CRH |= GPIO_CRH_MODE11_0;
}

void power_0_4() {
    GPIOA->BSRR = GPIO_BSRR_BS0;
    GPIOA->BSRR = GPIO_BSRR_BS1;
    GPIOA->BSRR = GPIO_BSRR_BS2;
    GPIOA->BSRR = GPIO_BSRR_BS3;
    GPIOA->BSRR = GPIO_BSRR_BS4;
}

void unpower_0_4() {
    GPIOA->BSRR = GPIO_BSRR_BR0;
    GPIOA->BSRR = GPIO_BSRR_BR1;
    GPIOA->BSRR = GPIO_BSRR_BR2;
    GPIOA->BSRR = GPIO_BSRR_BR3;
    GPIOA->BSRR = GPIO_BSRR_BR4;
}

void power_5_9() {
    GPIOA->BSRR = GPIO_BSRR_BS5;
    GPIOA->BSRR = GPIO_BSRR_BS6;
    // GPIOA->BSRR = GPIO_BSRR_BS7;
    // GPIOA->BSRR = GPIO_BSRR_BS8;
    GPIOA->BSRR = GPIO_BSRR_BS9;
    GPIOA->BSRR = GPIO_BSRR_BS10;
    GPIOA->BSRR = GPIO_BSRR_BS11;
}

void unpower_5_9() {
    GPIOA->BSRR = GPIO_BSRR_BR5;
    GPIOA->BSRR = GPIO_BSRR_BR6;
    // GPIOA->BSRR = GPIO_BSRR_BR7;
    // GPIOA->BSRR = GPIO_BSRR_BR8;
    GPIOA->BSRR = GPIO_BSRR_BR9;
    GPIOA->BSRR = GPIO_BSRR_BR10;
    GPIOA->BSRR = GPIO_BSRR_BR11;
}

// called each time timer does its thing
extern "C" void TIM2_IRQHandler() {
    // if button pressed
    if (GPIOA->IDR & GPIO_IDR_IDR15) {
        unpower_5_9();
        // do the blinking
        if (GPIOA->ODR & GPIO_ODR_ODR0) {
            unpower_0_4();
        } else {
            power_0_4();
        }
    // if button not pressed
    } else {
        // do the blinking
        unpower_0_4();
        if (GPIOA->ODR & GPIO_ODR_ODR5) {
            unpower_5_9();
        } else {
            power_5_9();
        }
    }
    TIM2->SR &= ~TIM_SR_UIF; // reset the update ivent flag
}

int main() {
    RCC->APB2ENR |= RCC_APB2ENR_IOPAEN
                 |  RCC_APB2ENR_AFIOEN
                 |  RCC_APB2ENR_TIM1EN;
    RCC->APB1ENR |= RCC_APB1ENR_TIM2EN;

    // inits
    init_leds();

    NVIC_EnableIRQ(TIM2_IRQn);
    TIM2->PSC = 8000-1; // prescale clock to 1khz
    TIM2->ARR = 1000/9-1; // proc 1/9 sec
    TIM2->DIER = TIM_DIER_UIE; // enable interruptions
    TIM2->CR1 = TIM_CR1_CEN; // enable counter

    // PWM
    GPIOA->CRL &= ~(GPIO_CRL_MODE7 | GPIO_CRL_CNF7); // clear values
    GPIOA->CRL |= GPIO_CRL_MODE7_0 | GPIO_CRL_CNF7_1; // enable + configure port
    GPIOA->CRH &= ~(GPIO_CRH_MODE8 | GPIO_CRH_CNF8);
    GPIOA->CRH |= GPIO_CRH_MODE8_0 | GPIO_CRH_CNF8_1;
    AFIO->MAPR |= AFIO_MAPR_TIM1_REMAP_0; // make alt function proc on p7

    TIM1->PSC = 8000-1; // 1khz
    TIM1->ARR = 1000-1; // proc 1 sec
    TIM1->CCR1 = 250-1; // pulse length to 1/4 sec
    TIM1->CCMR1 |= TIM_CCMR1_OC1M_1 | TIM_CCMR1_OC1M_2; // enable PWM
    // enable capture/compare, invert polarity and complementary output
    TIM1->CCER |= TIM_CCER_CC1E | TIM_CCER_CC1P | TIM_CCER_CC1NE;
    TIM1->BDTR |= TIM_BDTR_MOE; // enable output
    TIM1->CR1 |= TIM_CR1_CEN; // enable counter

    while (true) {}

    return 0;
}