import axios from "axios";
/*
* Creates one reusable API client for the whole frontend.
* Keeps components cleaner by avoiding repeated base URLs.
* Makes future auth/header changes much easier.
*/
export const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 10000,
});