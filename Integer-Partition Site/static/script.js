document.addEventListener("DOMContentLoaded", function () {
  const selectionElement = document.getElementById("selection");
  const secondForm = document.getElementById("second-form");
  const integerInput = document.getElementById("integer");
  const partsInput = document.getElementById("parts");
  const distanceInput = document.getElementById("distance");
  const maxOnesInput = document.getElementById("max_ones");
  const counterOutput = document.getElementById("counter-output");
  const generatorOutput = document.getElementById("generator-output");

  selectionElement.addEventListener("change", function () {
    const selectedOption = selectionElement.value;
    toggleFormInputs(selectedOption);
  });

  secondForm.addEventListener("submit", function (event) {
    event.preventDefault();
    const selectedOption = selectionElement.value;
    const action = event.submitter.value;

    if (action === "counter") {
      handleCounterAction(selectedOption);
    } else if (action === "generator") {
      handleGeneratorAction(selectedOption);
    }
  });

  function toggleFormInputs(selectedOption) {
    integerInput.disabled = true;
    partsInput.disabled = true;
    distanceInput.disabled = true;
    maxOnesInput.disabled = true;

    if (
      selectedOption === "roger_ramanujan" ||
      selectedOption === "capparelli"
    ) {
      integerInput.disabled = false;
      partsInput.disabled = false;
    } else if (selectedOption === "roger_ramanujan_gordon") {
      integerInput.disabled = false;
      partsInput.disabled = false;
      distanceInput.disabled = false;
      maxOnesInput.disabled = false;
    }
  }

  function handleCounterAction(selectedOption) {
    const integer = integerInput.value;
    const parts = partsInput.value;

    // Send the data to the Flask backend using AJAX
    sendFormData(selectedOption, "counter", integer, parts);
  }

  function handleGeneratorAction(selectedOption) {
    const integer = integerInput.value;
    const parts = partsInput.value;
    const distance = distanceInput.value;
    const maxOnes = maxOnesInput.value;

    // Send the data to the Flask backend using AJAX
    sendFormData(
      selectedOption,
      "generator",
      integer,
      parts,
      distance,
      maxOnes
    );
  }

  function sendFormData(
    selection,
    action,
    integer,
    parts,
    distance = null,
    maxOnes = null
  ) {
    const formData = new FormData();
    formData.append("selection", selection);
    formData.append("action", action);
    formData.append("integer", integer);
    formData.append("parts", parts);
    if (distance !== null) {
      formData.append("distance", distance);
    }
    if (maxOnes !== null) {
      formData.append("max_ones", maxOnes);
    }

    fetch("/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.text())
      .then((data) => {
        if (action === "counter") {
          counterOutput.textContent = data;
        } else if (action === "generator") {
          generatorOutput.textContent = data;
        }
      })
      .catch((error) => console.error(error));
  }
});
