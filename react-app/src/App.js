

import {createContext} from "react";
import AppRouter from "./AppRouter";
import {observer} from "mobx-react-lite";
const BaseApiUrl = createContext("http://localhost/api/v1")



window.static_url = "http://localhost:8000/static"
window.base_api_url = "http://localhost:8000/api/v1"
function App() {
  return (
        <BaseApiUrl.Provider value={BaseApiUrl}>
          <AppRouter/>
        </BaseApiUrl.Provider>
  );
}

export default observer(App);
