import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class IntegrationTest {

    private WebDriver driver;

    @Before
    public void setUp() {
        // Set up the Chrome driver
        WebDriverManager.chromedriver().setup();
        driver = new ChromeDriver();
    }

    @Test
    public void testIntegration() {
        // Navigate to the frontend URL
        driver.get("http://localhost:3000");

        // Click the "Get Message" button
        WebElement button = driver.findElement(By.cssSelector("button"));
        button.click();

        // Wait for the message to be displayed
        WebElement messageElement = driver.findElement(By.id("message"));
        String message = messageElement.getText();

        // Verify the message content
        Assert.assertEquals("Hello from the backend!", message);
    }

    @After
    public void tearDown() {
        // Quit the driver
        if (driver != null) {
            driver.quit();
        }
    }

    public static void main(String[] args) {
        org.junit.runner.JUnitCore.main("IntegrationTest");
    }
}
