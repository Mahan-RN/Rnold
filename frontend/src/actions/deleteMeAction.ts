import { redirect } from "react-router";
import apiFetch from "src/api/Fetch";

export default async function deleteMeAction() {
    await apiFetch<void>("/users/me", { method: "DELETE" });
    return redirect("/");
}