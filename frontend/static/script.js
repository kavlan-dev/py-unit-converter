document.addEventListener("DOMContentLoaded", function () {
  // Tab switching functionality
  const tabButtons = document.querySelectorAll(".tab-button");
  const tabPanes = document.querySelectorAll(".tab-pane");

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const tabId = button.getAttribute("data-tab");

      // Remove active class from all buttons and panes
      tabButtons.forEach((btn) => btn.classList.remove("active"));
      tabPanes.forEach((pane) => pane.classList.remove("active"));

      // Add active class to clicked button and corresponding pane
      button.classList.add("active");
      document.getElementById(tabId).classList.add("active");
    });
  });

  // Form submission handlers
  const forms = document.querySelectorAll(".converter-form");
  forms.forEach((form) => {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      const formId = form.id;
      const converterType = formId.split("-")[0]; // 'length', 'weight', or 'temperature'

      // Get form data
      const formData = new FormData(form);
      const data = {
        value: parseFloat(formData.get("value")),
        from_unit: formData.get("from_unit"),
        to_unit: formData.get("to_unit"),
      };

      try {
        const backendUrl = "/api";

        const response = await fetch(`${backendUrl}/convert/${converterType}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();

        // Display result
        const resultElement = document.getElementById(
          `${converterType}-result`,
        );
        resultElement.innerHTML = `
                    <strong>${data.value} ${data.from_unit}</strong> =
                    <strong>${result.result} ${data.to_unit}</strong>
                `;
        resultElement.style.display = "block";
      } catch (error) {
        console.error("Error:", error);
        const resultElement = document.getElementById(
          `${converterType}-result`,
        );
        resultElement.innerHTML = `Error: ${error.message}`;
        resultElement.style.display = "block";
        resultElement.style.color = "#e74c3c";
      }
    });
  });
});
