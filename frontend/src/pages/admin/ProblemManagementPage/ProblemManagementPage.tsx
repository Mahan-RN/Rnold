import UploadProblemForm from "src/components/admin/UploadProblemForm/UploadProblemForm";
import styles from "src/pages/admin/ProblemManagementPage/ProblemManagementPage.module.css";

export default function ProblemManagementPage() {
    return (
        <div className={styles.flexContainer}>
            <h1>Problem Management</h1>
            <UploadProblemForm />
        </div>
    );
}
