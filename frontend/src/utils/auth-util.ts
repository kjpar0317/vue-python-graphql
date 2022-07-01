export function isAuthenticated() {
  // axios
  //   .post(`api/token/validate`, {}, { withCredentials: true })
  //   .then((resp) => resp.statusText == "OK")
  //   .catch((err) => false);

  return sessionStorage.getItem("token");
}
