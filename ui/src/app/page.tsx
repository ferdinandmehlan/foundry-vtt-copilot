"use client";

import {CopilotSidebar} from "@copilotkit/react-core/v2";

export default function Home() {
  return (
    <div className="flex flex-1 items-center justify-center p-4">
        <CopilotSidebar
            defaultOpen={true}
            // Adds an initial message to the chat
            labels={{
                modalHeaderTitle: "Popup Assistant",
                welcomeMessageText:
                    "👋 Hi, there! You're chatting with an Agno agent.",
            }}
        />
    </div>
  );
}
