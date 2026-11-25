import axios from "axios";
import { type ActionFunctionArgs, redirect } from "react-router";

export default async function profilePageAction({
    request,
}: ActionFunctionArgs) {
    const formData = await request.formData();
    const intent = formData.get("intent");

    if (intent === "delete-me") {
        await axios.delete<void>("/api/users/me");
        return redirect("/");
    } else if (intent === "delete-submissions") {
        await axios.delete<void>("/api/submissions/me");
    } else {
        throw Error("Unexpected error in Profile Page action.");
    }
}
