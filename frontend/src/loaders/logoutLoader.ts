import { redirect } from "react-router";

export default function logoutLoader() {
    return redirect("/");
}
