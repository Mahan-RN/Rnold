import { WebR } from "webr";

let instance: Promise<WebR> | null = null;

export default async function getWebR(): Promise<WebR> {
    if (instance === null) {
        const webR = new WebR();
        instance = (async () => {
            await webR.init();
            await webR.installPackages(["testthat"]);
            return webR;
        })();
        instance.catch(() => {
            instance = null;
        });
    }

    return instance;
}
