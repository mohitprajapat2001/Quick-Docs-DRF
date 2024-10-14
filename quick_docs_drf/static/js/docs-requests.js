function docsGetRequest(url, callBack, errorHandle) {
  /* Standart Get Request Function */
  docsAjaxRequest("GET", url, null, callBack, errorHandle);
}

function docsPostRequest(url, data, callBack, errorHandle) {
  /* Standart Post Request Function */
  docsAjaxRequest("POST", url, data, callBack, errorHandle);
}
function docsPutRequest(url, data, callBack, errorHandle) {
  /* Standart Put Request Function */
  docsAjaxRequest("PUT", url, data, callBack, errorHandle);
}
function docsPatchRequest(url, data, callBack, errorHandle) {
  /* Standart Patch Request Function */
  docsAjaxRequest("PATCH", url, data, callBack, errorHandle);
}
function docsDeleteRequest(url, callBack, errorHandle) {
  /* Standart Delete Request Function */
  docsAjaxRequest("DELETE", url, null, callBack, errorHandle);
}
function docsOptionsRequest(url, callBack, errorHandle) {
  /* Standart Options Request Function */
  docsAjaxRequest("OPTIONS", url, null, callBack, errorHandle);
}

function docsAjaxRequest(type, url, data, callBack, errorHandle) {
  const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  /*Standart Ajax Request Function */
  $.ajax({
    url: url,
    type: type,
    data: data,
    headers: {
      "X-CSRFToken": csrfToken,
      Authorization: window.localStorage.getItem("Authorization"),
    },
    success: function (response, status, xhr) {
      if (xhr.status != 204) {
        if (callBack) {
          callBack(xhr);
        }
      }
    },
    error: function (xhr, status, error) {
      console.error("Error occurred:", xhr.responseText, status, error);
      if (errorHandle) {
        errorHandle(xhr);
      }
    },
  });
}
