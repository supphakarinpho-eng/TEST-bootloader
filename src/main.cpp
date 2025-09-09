#include <Arduino.h>
#include <version.h>
#include "esp_log.h"

constexpr char TAG[] = "TEST";

void setup() {

    Serial.begin(115200);

    ESP_LOGI(TAG, "Starting Program");
    ESP_LOGE(TAG, "LOG ERROR");

    Serial.println();
    Serial.println("\t---------------------------------");
    Serial.printf("\tFirmware Build Number: %d\n", BUILD_NUMBER);
    Serial.printf("\tBuild Date: %s\n", BUILD_DATE);
    Serial.println("\t---------------------------------");
    Serial.println();

    constexpr auto age{15};

    [=]() {
        Serial.printf("Lambda expressions : age = %d\n", age);
    }();

    constexpr int number_arr[] = {1, 2, 3, 4, 5};
    for (const auto &element: number_arr) {
        Serial.printf("element %d\n", element);
    }

    ESP_LOGI(TAG, "Ending Program");
}

void loop() {
    // ...
}
