#include "main.h"

// change the GPIO pins with need
// Function prototypes
void SystemClock_Config(void);
static void MX_GPIO_Init(void);

int main(void)
{
    // Initialize the HAL Library
    HAL_Init();

    // Configure the system clock
    SystemClock_Config();

    // Initialize all configured peripherals
    MX_GPIO_Init();

    // Infinite loop
    while (1)
    {
        // Activate the Red LED connected to D6 (PA6)
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, GPIO_PIN_SET);  // Set PA6 high
        HAL_Delay(1000);  // Delay for 1 second

        // Deactivate the Red LED
        HAL_GPIO_WritePin(GPIOA, GPIO_PIN_6, GPIO_PIN_RESET); // Set PA6 low
        HAL_Delay(1000);  // Delay for 1 second
    }
}

// GPIO Initialization Function
static void MX_GPIO_Init(void)
{
    // GPIO Ports Clock Enable
    __HAL_RCC_GPIOA_CLK_ENABLE();

    // Configure PA6 as output
    GPIO_InitTypeDef GPIO_InitStruct = {0};
    GPIO_InitStruct.Pin = GPIO_PIN_6;          // Pin D6 (PA6)
    GPIO_InitStruct.Mode = GPIO_MODE_OUTPUT_PP; // Push-Pull Output
    GPIO_InitStruct.Pull = GPIO_NOPULL;        // No Pull-up or Pull-down resistors
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW; // Low speed
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);    // Initialize GPIO
}

// System Clock Configuration
void SystemClock_Config(void)
{
    // Configuration code for system clock (can be generated using STM32CubeMX)
    // This can be left empty for simple GPIO toggle
}
