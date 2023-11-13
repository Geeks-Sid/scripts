#include <opencv2/opencv.hpp>
#include <iostream>
#include <vector>
#include <string>
#include <filesystem>

namespace fs = std::filesystem;

int main()
{
    std::string image_path = "./large_image.png"; // Replace with your image path

    // Load the image
    cv::Mat image = cv::imread(image_path, cv::IMREAD_GRAYSCALE);
    if (image.empty())
    {
        std::cerr << "Could not read the image: " << image_path << std::endl;
        return 1;
    }

    // Find unique values in the image
    std::vector<uchar> unique_values;
    for (int y = 0; y < image.rows; ++y)
    {
        for (int x = 0; x < image.cols; ++x)
        {
            uchar val = image.at<uchar>(y, x);
            if (std::find(unique_values.begin(), unique_values.end(), val) == unique_values.end())
            {
                unique_values.push_back(val);
            }
        }
    }

    // Process and save images for each unique value
    for (uchar value : unique_values)
    {
        cv::Mat processed_image = (image == value) / 255 * 255; // Replace pixels

        std::string save_path = "./processed_image_" + std::to_string(value) + ".png";
        cv::imwrite(save_path, processed_image);
    }

    return 0;
}
