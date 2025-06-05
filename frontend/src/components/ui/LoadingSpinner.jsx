import { Spinner, Center, Text, VStack } from '@chakra-ui/react';

/**
 * Loading spinner component
 * 
 * @param {object} props - Component props
 * @param {string} props.text - Text to display under the spinner
 * @returns {JSX.Element} LoadingSpinner component
 */
const LoadingSpinner = ({ text = 'Loading...' }) => {
  return (
    <Center py={10}>
      <VStack spacing={3}>
        <Spinner
          thickness="4px"
          speed="0.65s"
          emptyColor="gray.200"
          color="brand.500"
          size="xl"
        />
        <Text color="gray.600">{text}</Text>
      </VStack>
    </Center>
  );
};

export default LoadingSpinner; 