import React, { useEffect, useRef, useState } from "react"
import BaseModal from "./BaseModal"
import { isFirstAccess, neverShowTutorial } from "../lib/tutorialManager"

const TutorialModal: React.VFC = () => {
  const [openTutorialModal, setOpenTutorialModal] = useState(false)
  const [neverShow, setNeverShow] = useState(true)
  const buttonRef = useRef<HTMLButtonElement | null>(null)

  useEffect(() => {
    if (isFirstAccess()) {
      setOpenTutorialModal(true)
    }
  }, [])

  const handleClose = () => {
    setOpenTutorialModal(false)
    if (neverShow) {
      neverShowTutorial()
    }
  }

  return (
    <BaseModal
      open={openTutorialModal}
      onClose={() => setOpenTutorialModal(false)}
      initialFocus={buttonRef}
    >
      <div className="flex flex-col items-center space-y-4 overflow-hidden rounded-lg">
        <h1 className="text-2xl">使い方</h1>
        <p>いくつかの簡単な質問に答えることで、おすすめの夏休みの使い方を提案します！</p>
        <div>
          <label className="flex items-center space-x-1 text-sm text-gray-900">
            <input
              type="checkbox"
              checked={neverShow}
              onChange={(e) => setNeverShow(e.target.checked)}
            />
            <span>次回以降は表示しない</span>
          </label>
        </div>
        <div className="mt-4">
          <button
            className="mb-4"
            onClick={handleClose}
            ref={buttonRef}
          >
            とじる
          </button>
        </div>
      </div>
    </BaseModal>
  )
}

export default TutorialModal
