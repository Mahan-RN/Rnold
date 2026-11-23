import axios from "axios";
import type { ActionFunctionArgs } from "react-router";

export default async function problemPageAction({
    request,
}: ActionFunctionArgs) {
    const body = await request.json();
    if (body.problemID === null || body.accepted === null) {
        throw new Error(
            "Failed to send create submission request for server. One of the required fields was null.",
        );
    }
    await axios.post("/api/submissions", {
        problem_id: body.problemID,
        accepted: body.accepted,
    });

    return null;
}
