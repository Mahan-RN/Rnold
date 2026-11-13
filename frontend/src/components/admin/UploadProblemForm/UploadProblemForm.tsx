import { Form, useNavigation } from "react-router";
import styles from "src/components/admin/UploadProblemForm/UploadProblemForm.module.css";

export default function UploadProblemForm() {
    const navigation = useNavigation();
    const isSubmitting = navigation.state === "submitting";

    return (
        <Form
            method="POST"
            encType="multipart/form-data"
            className={styles.flexContainer}
        >
            <div className={styles.header}>
                <h2>Upload a Problem</h2>
                <p>
                    Upload an R file containing the problem template and its
                    test cases.
                </p>
            </div>
            <div className={styles.fileSection}>
                <label htmlFor="file">Problem file</label>
                <input type="file" id="file" name="file" accept=".R" required />
                <span className={styles.hint}>
                    Accepted format: .R · Maximum size: 15 KB
                </span>
            </div>

            <button
                type="submit"
                name="intent"
                value="submit-file"
                className={styles.submitButton}
                disabled={isSubmitting}
            >
                {isSubmitting ? "Uploading..." : "Upload Problem"}
            </button>
        </Form>
    );
}
