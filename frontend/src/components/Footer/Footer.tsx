import styles from "src/components/Footer/Footer.module.css";

export default function Footer() {
    return (
        <footer className={styles.root}>
            <p>
                ©2026 Mahan Rafieenaini (
                <a
                    href="https://github.com/Mahan-RN"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    GitHub
                </a>{" "}
                |{" "}
                <a
                    href="https://www.linkedin.com/in/mahan-rafieenaini/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    LinkedIn
                </a>
                ). Licensed under GPL-3.0.
            </p>
        </footer>
    );
}
