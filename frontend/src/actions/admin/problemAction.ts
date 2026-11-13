import type { ActionFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

interface UploadFileResponse {
    message: string;
}

export default async function problemAction({ request }: ActionFunctionArgs) {
    const formData = await request.formData();
    const intent = formData.get("intent");

    if (intent === "submit-file") {
        const file = formData.get("file");

        if (!(file instanceof File)) {
            return { success: false, error: "Please select a file." };
        }

        if (!file.name.toLocaleLowerCase().endsWith(".r")) {
            return { success: false, error: "Only R files are accepted" };
        }

        if (file.size > 15 * 1024) {
            return {
                success: false,
                error: "File must not be larger than 15 KB.",
            };
        }

        const backendFormData = new FormData();
        backendFormData.append("file", file);

        try {
            const result = await apiFetch<UploadFileResponse>(
                "/problems/files",
                {
                    method: "POST",
                    body: backendFormData,
                },
            );
            return { success: true, message: result.message };
        } catch (error) {
            if (error instanceof Response) {
                return {
                    success: false,
                    error: await error.text(),
                };
            }
        }

        return { success: false, error: "An unexpected error occured." };
    }

    return { success: false, error: "Invalid action." };
}
