import type { ActionFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export default async function deleteUserAction({
    request,
}: ActionFunctionArgs) {
    const formData = await request.formData();
    const github_id = formData.get("github_id");

    try {
        await apiFetch<string | undefined>(`/users/${github_id}`, {
            method: "DELETE",
        });
        return {
            success: true,
            message: `User with GitHub ID ${github_id} deleted successfully`,
        };
    } catch (error) {
        if (error instanceof Response) {
            const message = await error.text();
            return {
                success: false,
                message: message,
            };
        }

        throw error;
    }
}
