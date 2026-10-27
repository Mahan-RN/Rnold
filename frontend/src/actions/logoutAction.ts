import { redirect } from "react-router";
import apiFetch from "src/api/Fetch";

export default async function logoutAction() {
    await apiFetch<void>("/auth/github/logout", { method: "POST" });
    return redirect("/");
}
