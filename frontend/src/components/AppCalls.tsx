// src/components/AppCalls.tsx
// AppCalls.tsx
import './AppCalls.css'; 
import React, { useState } from 'react';
import algosdk from 'algosdk';
import { useSnackbar } from 'notistack';
import { useWallet } from '@txnlab/use-wallet';
import * as algokit from '@algorandfoundation/algokit-utils';
import { getAlgodConfigFromViteEnvironment } from '../utils/network/getAlgoClientConfigs';

const AppCalls = ({ appID, setAppID }) => {
  const [loading, setLoading] = useState(false);
  const [certificateCount, setCertificateCount] = useState(0);
  const algodConfig = getAlgodConfigFromViteEnvironment();
  const algodClient = algokit.getAlgoClient(algodConfig);
  const { enqueueSnackbar } = useSnackbar();
  const { signer, activeAddress } = useWallet();
  const sender = { signer, addr: activeAddress! };

  // Add the rest of the relevant methods and logic here...

  const createCertificate = async () => {
    setLoading(true);

    // Implement the interaction with the Algorand smart contract here.
    // This should include creating a transaction to call the create_certificate subroutine.
    // After executing the transaction, retrieve the updated certificate count and set it using setCertificateCount.

    setLoading(false);
  };

  return (
    <div className="app-calls-container">
      <button onClick={createCertificate} disabled={loading}>
        Create Certificate
      </button>

      <div>
        <p>Certificate Count: {certificateCount}</p>
      </div>
    </div>
  );
};

export default AppCalls;
