/*Constants */
const apiResult = document.getElementById("api-result");
const apiUrl = document.getElementById("api-url").value;

function loadAPI() {
  const apiUrl = document.getElementById("api-url").value;
  if (apiUrl) {
    /*Check for Relative URL */
    if (apiUrl.startsWith("/")) {
      docsGetRequest(apiUrl, docsHandleApiResult, handleExceptionsDocs);
      /*URL Perfect */
    } else {
      /*Not Relative URL */
      triggerAlert("Please Enter Relative Path");
    }
  } else {
    /*URL Input Empty */
    triggerAlert("Please Enter a URL");
  }
}
